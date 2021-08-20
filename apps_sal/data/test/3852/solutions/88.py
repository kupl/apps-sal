def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    if min(A) >= 0:
        v = float('-inf')
        max_i = None
        for i in range(N):
            if A[i] > v:
                max_i = i
                v = A[i]
        ans.append([max_i, 0])
        for i in range(1, N):
            ans.append([i - 1, i])
    elif max(A) <= 0:
        v = float('inf')
        min_i = None
        for i in range(N):
            if A[i] < v:
                min_i = i
                v = A[i]
        ans.append([min_i, N - 1])
        for i in range(N - 2, -1, -1):
            ans.append([i + 1, i])
    elif abs(max(A)) >= abs(min(A)):
        v = float('-inf')
        max_i = None
        for i in range(N):
            if A[i] > v:
                max_i = i
                v = A[i]
        for i in range(N):
            if i != max_i:
                ans.append([max_i, i])
        ans.append([max_i, max_i])
        ans.append([max_i, 0])
        for i in range(1, N):
            ans.append([i - 1, i])
    else:
        v = float('inf')
        min_i = None
        for i in range(N):
            if A[i] < v:
                min_i = i
                v = A[i]
        for i in range(N):
            if i != min_i:
                ans.append([min_i, i])
        ans.append([min_i, min_i])
        ans.append([min_i, N - 1])
        for i in range(N - 2, -1, -1):
            ans.append([i + 1, i])
    print(len(ans))
    for (i, j) in ans:
        print(str(i + 1) + ' ' + str(j + 1))


def __starting_point():
    main()


__starting_point()
