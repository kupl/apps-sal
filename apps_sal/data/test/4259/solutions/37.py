K = int(input())
(A, B) = map(int, input().split())
print('NOGK'[K < B - A + 2 or B % K < A % K or B % K == 0 or (A % K == 0)::2])
