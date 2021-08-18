def f(myList):
    if len(myList) == 0:
        return 0
    else:
        tmp = min(myList)
        ans = tmp
        for i in range(len(myList)):
            myList[i] -= tmp
        newList = []
        for i in range(len(myList)):
            pop_a = myList.pop()
            if pop_a != 0:
                newList.append(pop_a)
            else:
                ans += f(newList)
                newList = []
        ans += f(newList)
        return ans


n = int(input())
a = list(map(int, input().split()))

print((f(a)))
