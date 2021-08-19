def main():
    N = int(input())
    L = [int(l) for l in input().split(' ')]
    cnt = 0
    L.sort()
    for i in range(len(L)):
        for j in range(i + 1, len(L)):
            for k in range(j + 1, len(L)):
                if L[k] < L[i] + L[j] and L[i] != L[j] and (L[j] != L[k]):
                    cnt += 1
    print(cnt)


main()
