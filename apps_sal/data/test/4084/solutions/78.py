N, A, B = map(int, input().split())
times, residue = divmod(N, A+B)
blue = times*A + min(residue, A)
print(blue)
