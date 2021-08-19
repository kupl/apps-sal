K = int(input())
frag = [0] * (K + 1)
frag[1] = 7 % K
for i in range(2, K + 1):
    frag[i] = (frag[i - 1] * 10 + 7) % K
for i in range(1, K + 1):
    if frag[i] == 0:
        print(i)
        break
else:
    print(-1)
