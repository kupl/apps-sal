S = input()
a = int(input())
List = list(S)
res = 1
for i in range(a):
    if List[i] != "1":
        res = List[i]
        break
print(res)
