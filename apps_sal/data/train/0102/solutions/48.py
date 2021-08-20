t = int(input())
answer = []
for i in range(t):
    n = input()
    k = (len(n) - 1) * 9 + int(n[0])
    if int(n[0] * len(n)) > int(n):
        k -= 1
    answer.append(k)
for i in answer:
    print(i)
