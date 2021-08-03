N = int(input())
p = list(map(int, input().split()))

if p == sorted(p):
    print('YES')
else:
    ret = 'NO'
    is_sorted = False
    # 全通りの組み合わせをみて、昇順かどうか調べる
    for i in range(N - 1):
        for j in range(i + 1, N):
            # p[i]とp[j]より小さければ抜ける
            if p[i] < p[j]:
                continue
            else:
                k = p.copy()
                k[i], k[j] = k[j], k[i]

#             for l in range(N-1):
#                 if k[l+1] < k[l]:
#                     is_sorted = False
#                     break

            if k == sorted(p):
                ret = 'YES'
                is_sorted = True
                break
        if is_sorted:
            break

    print(ret)
