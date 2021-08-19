n = int(input())
ws = set((''.join(sorted(set(w))) for w in input().split()))
print(len(ws))
