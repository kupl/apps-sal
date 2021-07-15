a, b, c = map(int, input().split())

res = [abs(a-b), abs(a-c), abs(b-c)]

print(sum(res)-max(res))  
