class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        gLefts = dict()
        gRights = dict()
        gSizeCounter = collections.Counter()
        result = -1
        for step, x in enumerate(arr, 1):
            try:
                rGroup = gLefts[x + 1]
            except KeyError:
                rGroup = None
            try:
                lGroup = gRights[x - 1]
            except KeyError:
                lGroup = None

            if lGroup is not None and rGroup is not None:
                lSize = lGroup[2]
                rSize = rGroup[2]
                del gLefts[rGroup[0]]
                del gRights[lGroup[1]]

                gSizeCounter[lSize] -= 1

                gSizeCounter[rSize] -= 1

                lSize += 1 + rSize
                gSizeCounter[lSize] += 1
                lGroup[2] = lSize
                lGroup[1] = rGroup[1]
                gRights[lGroup[1]] = lGroup
            elif lGroup is not None:
                lSize = lGroup[2]

                gSizeCounter[lSize] -= 1

                lSize += 1
                gSizeCounter[lSize] += 1
                lGroup[2] = lSize
                del gRights[lGroup[1]]
                lGroup[1] = x
                gRights[x] = lGroup
            elif rGroup is not None:
                rSize = rGroup[2]

                gSizeCounter[rSize] -= 1

                rSize += 1
                gSizeCounter[rSize] += 1
                rGroup[2] = rSize
                del gLefts[rGroup[0]]
                rGroup[0] = x
                gLefts[x] = rGroup
            else:
                gSizeCounter[1] += 1
                gLefts[x] = gRights[x] = [x, x, 1]

            if gSizeCounter[m] > 0:
                result = step

        return result
