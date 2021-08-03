n = int(input())
ai = list(map(int, input().split()))
bi = list(map(int, input().split()))
ai2 = [0] * (n + 1)
n2 = 0
for i in range(n):
    num = 0
    if ai2[bi[i]] != 1:
        for j in range(n2, n):
            ai2[ai[j]] = 1
            if ai[j] == bi[i]:
                num = j + 1 - n2
                n2 = j + 1
                break
    print(num, end=" ")
