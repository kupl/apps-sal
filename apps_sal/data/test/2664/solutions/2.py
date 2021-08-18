import sys
import random
balls = list(map(str, list(range(1, 6))))
answered = 1

print('1')
mid = len(balls) / 2
print('3 1 2 2')
print('3 3 3 4')
sys.stdout.flush()
ans = int(input().strip())

if ans == 0:
    print('2')
    print('5')
    sys.stdout.flush()
if ans == 2:
    print('2')
    print('2')
    sys.stdout.flush()
if ans == 1:
    print('2')
    print('1')
if ans == -1:
    print('2')
    print('4')
if ans == -2:
    print('2')
    print('3')
