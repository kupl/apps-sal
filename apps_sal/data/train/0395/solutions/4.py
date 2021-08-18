class Solution(object):
    def oddEvenJumps(self, A):
        lenOfA = len(A)
        sortedA = sorted(range(lenOfA), key=lambda key: A[key])

        def make(array):
            toNextIndex = [None] * lenOfA
            stack = []
            for i in array:
                while stack and i > stack[-1]:
                    toNextIndex[stack.pop()] = i
                stack.append(i)
            return toNextIndex
        nextOdd = make(sortedA)
        sortedA.sort(key=lambda key: -A[key])
        nextEven = make(sortedA)

        def update(memo, footPrints):
            for footPrint in footPrints:
                memo['%d-%s' % (footPrint[0], footPrint[1])] = None

        success = {}
        failed = {}
        output = 0
        for startIndex in range(lenOfA):
            index = startIndex
            jump = 1
            footPrints = set([])
            while index < lenOfA:
                if index == lenOfA - 1:
                    update(success, footPrints)
                    output += 1
                    break

                isOdd = jump % 2 == 1
                cacheKey = '%d-odd' % index if isOdd else '%d-even' % index
                if cacheKey in success:
                    output += 1
                    break
                elif cacheKey in failed:
                    break

                if isOdd:
                    nextIndex = nextOdd[index]
                    if nextIndex is None:
                        update(failed, footPrints)
                        break
                    footPrints.add((index, 'odd'))
                else:
                    nextIndex = nextEven[index]
                    if nextIndex is None:
                        update(failed, footPrints)
                        break
                    footPrints.add((index, 'even'))

                index = nextIndex
                jump += 1

        return output
