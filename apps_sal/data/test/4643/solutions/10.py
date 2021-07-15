import time

def busy_wait(dt):
    current_time = time.time()
    while (time.time() < current_time+dt):
        pass

a = list(map(int, input().split()))
a = a[1:]
busy_wait(1.8)
a.sort()
w = len(str(max(a)))
print(a[0], end='')
for x in a[1:]:
    print(str(x).rjust(w + 1), end='')
print()

