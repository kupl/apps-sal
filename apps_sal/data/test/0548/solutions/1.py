n = int(input())
a = [int(v) for v in input().split()]

s = 0
was_odd = False
for v in a:
    s += v
    if (v & 1):
        was_odd = True

if s % 2 == 1:
    print("First")
else:
    if was_odd:
        print("First")
    else:
        print("Second")
