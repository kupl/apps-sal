(N, M) = map(int, input().split())
if M >= 0:
    a_list = [i for i in range(M + 1, M + N)]
elif N + M > 0:
    a_list = [i for i in range(M, M + N)]
else:
    a_list = [i for i in range(M, M + N - 1)]
print(sum(a_list))
