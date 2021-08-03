class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed:
            return True

        temp = []
        i = popiter = 0
        while i < len(pushed):
            if temp and temp[-1] == popped[popiter]:
                print(temp, popped[popiter])
                temp.pop()
                popiter += 1
            else:
                temp.append(pushed[i])
                i += 1

        print(temp, popiter)
        while temp:
            if temp[-1] == popped[popiter]:
                temp.pop()
                popiter += 1
            else:
                return False
        return True
