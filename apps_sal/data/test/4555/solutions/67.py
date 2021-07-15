a, b, k = (int(i) for i in input().split())
list_ans = []
for i in range(1, k + 1):
    if a == b:
        list_ans.append(a)
        break
    if a > b: break
    list_ans.append(a)
    list_ans.append(b)
    a = a + 1
    b = b - 1

for i in sorted(list_ans): print(i)
