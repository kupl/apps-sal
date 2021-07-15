N, M = map(int, input().split())
 
wating_time = 1900 * M + 100 * (N-M)
print(2**M*wating_time)
