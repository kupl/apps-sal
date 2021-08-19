(N, A, B) = list(map(int, input().split()))
sets = N // (A + B)
a_count = A * sets
mod = N % (A + B)
a_count += mod if mod < A else A
print(a_count)
