class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        mystr = [0] * len(arr)
        latest = -1
        mydict = {}
        count = 0
        for i in range(len(arr)):
            mystr[arr[i] - 1] = 1
            if arr[i] - 2 not in mydict.keys() and arr[i] not in mydict.keys():
                mydict[arr[i] - 1] = [arr[i] - 1, arr[i] - 1, False]
                if m == 1:
                    count += 1
                    mydict[arr[i] - 1] = [arr[i] - 1, arr[i] - 1, True]

            elif arr[i] - 2 in mydict.keys() and arr[i] not in mydict.keys():
                head = mydict[arr[i] - 2][0]
                if mydict[arr[i] - 2][2] == True:
                    count -= 1
                del mydict[arr[i] - 2]
                mydict[head] = [head, arr[i] - 1, False]
                mydict[arr[i] - 1] = [head, arr[i] - 1, False]
                if arr[i] - head == m:
                    count += 1
                    mydict[head] = [head, arr[i] - 1, True]
                    mydict[arr[i] - 1] = [head, arr[i] - 1, True]

            elif arr[i] - 2 not in mydict.keys() and arr[i] in mydict.keys():
                tail = mydict[arr[i]][1]
                if mydict[arr[i]][2] == True:
                    count -= 1
                del mydict[arr[i]]
                mydict[tail] = [arr[i] - 1, tail, False]
                mydict[arr[i] - 1] = [arr[i] - 1, tail, False]
                if tail - (arr[i] - 1) + 1 == m:
                    count += 1
                    mydict[tail] = [arr[i] - 1, tail, True]
                    mydict[arr[i] - 1] = [arr[i] - 1, tail, True]

            else:
                head = mydict[arr[i] - 2][0]
                tail = mydict[arr[i]][1]
                if mydict[arr[i] - 2][2] == True:
                    count -= 1
                if mydict[arr[i]][2] == True:
                    count -= 1
                del mydict[arr[i] - 2]
                del mydict[arr[i]]

                mydict[head] = [head, tail, False]
                mydict[tail] = [head, tail, False]
                if tail - head + 1 == m:
                    count += 1
                    mydict[head] = [head, tail, True]
                    mydict[tail] = [head, tail, True]
            if count > 0:
                latest = i + 1
        return(latest)
