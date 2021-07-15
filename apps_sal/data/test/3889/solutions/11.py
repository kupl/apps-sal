n = int(input())
s = input().strip()

print(['Yes', 'No'][n > 1 and len(set(s)) == n])

