def main():
    n = int(input())
    A = [int(a) for a in input().split(' ')]
    A.sort(reverse=True)
    ans = []
    f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    if A[0] <= 10:
        for i in range(n):
            for j in range(i + 1, n):
                ans.append({'max': A[i], 'min': A[j], 'comb': int(f[A[i]] / (f[A[j]] * f[A[i] - A[j]]))})
        ans.sort(key=lambda s: -s['comb'])
        print(ans[0]['max'], ans[0]['min'])
        return 0
    i = 0
    j = 1
    while i < n and j < n:
        M = A[i]
        m = A[j]
        if abs(A[i] / 2 - A[j]) <= 0.5:
            ans.append({'max': A[i], 'min': A[j], 'dif': abs(A[i] / 2 - A[j]), 'k': min([A[j], A[i] - A[j]])})
            i += 1
        elif A[i] / 2 < A[j]:
            if j < n - 1:
                j += 1
            else:
                ans.append({'max': A[i], 'min': A[j], 'dif': abs(A[i] / 2 - A[j]), 'k': min([A[j], A[i] - A[j]])})
                j += 1
        elif A[i] / 2 > A[j]:
            if abs(A[i] / 2 - A[j - 1]) > abs(A[i] / 2 - A[j]) or j == i + 1:
                ans.append({'max': A[i], 'min': A[j], 'dif': abs(A[i] / 2 - A[j]), 'k': min([A[j], A[i] - A[j]])})
            else:
                ans.append({'max': A[i], 'min': A[j - 1], 'dif': abs(A[i] / 2 - A[j - 1]), 'k': min([A[j - 1], A[i] - A[j - 1]])})
            i += 1
        if i == j:
            j += 1
    ans.sort(key=lambda s: (-s['k'], -s['max']))
    k_cand1 = ans[0]['k']
    ans2_idx = 0
    for i in range(len(ans)):
        if ans[i]['k'] == k_cand1 - 1:
            ans2_idx = i
    if ans2_idx and ans[0]['max'] < ans[i]['max']:
        print(ans[i]['max'], ans[i]['min'])
    else:
        print(ans[0]['max'], ans[0]['min'])


main()
