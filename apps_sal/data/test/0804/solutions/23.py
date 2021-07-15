s = input()
k = int(input())
flag = 0
if len(s) < k:
    print('impossible')
    flag = 1
list1 = set()
if not flag:
    for i in range(len(s)):
        list1.add(s[i])
    if k - len(list1) < 0:
        print(0)
    else:
        print(k - len(list1))
