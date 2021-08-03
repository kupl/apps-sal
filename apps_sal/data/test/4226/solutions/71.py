import sys
vol, foot = map(int, input().split())
for i in range(vol + 1):
    if 2 * i + 4 * (vol - i) == foot:
        print("Yes")
        return

print("No")
