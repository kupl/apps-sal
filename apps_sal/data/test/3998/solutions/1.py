import collections


def temp(list1):
    list2 = list(list1)
    list3 = []
    cnt = collections.Counter()
    for i in range(len(list1)):
        cnt[list1[i]] += 1
    tep = max(list1)
    if cnt[tep] != 1:
        if cnt[tep] <= 5:
            for i in range(5):
                if tep in list2:
                    list3.append(list2.index(tep))
                    list2[list2.index(tep)] = -1
                else:
                    break
        else:
            for i in range(4):
                if tep in list2:
                    list3.append(list2.index(tep))
                    list2[list2.index(tep)] = -1
                else:
                    break
    else:
        list3.append(list1.index(tep))
        list2.remove(tep)
        list3.append(list1.index(max(list2)))
    return list3


n = int(input())
intgrade = list(map(int, input().split()))
bitlists = []

if len(set(intgrade)) == 1:
    print(intgrade[0])
    print(0)

else:
    while len(set(intgrade)) != 1:
        listA = temp(intgrade)
        bitlist = ''

        for i in range(len(listA)):
            if intgrade[listA[i]] > 0:
                intgrade[listA[i]] -= 1

        for i in range(n):
            if i in listA:
                bitlist += "1"
            else:
                bitlist += "0"
        bitlists.append(bitlist)
    print(intgrade[0])
    print(len(bitlists))
    for i in range(len(bitlists)):
        print(bitlists[i])
