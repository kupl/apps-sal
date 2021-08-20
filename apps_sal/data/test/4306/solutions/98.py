(A, B, C, D) = map(int, input().split())
init = max(A, C)
end = min(B, D)
print(end - init if init < end else 0)
