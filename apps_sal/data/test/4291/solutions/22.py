n, q = map(int, input().split())
s = input()
cusumList = [0]
for i in range(n - 1):
    if s[i] == "A" and s[i + 1] == "C":
        cusumList.append(cusumList[i] + 1)
    else:
        cusumList.append(cusumList[i])

for i in range(q):
    l, r = map(int, input().split())
    print(cusumList[r - 1] - cusumList[l - 1])
