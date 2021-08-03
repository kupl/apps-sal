r, g, b = list(map(int, input().split()))
print(('YES' if int(r * 100 + 10 * g + b) % 4 == 0 else 'NO'))
