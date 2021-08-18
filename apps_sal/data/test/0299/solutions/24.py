'''
@author: linhz
Greg's Workout
http://codeforces.com/problemset/problem/255/A
'''
n = int(input())
exercise = list(map(int, input().split()))
res = [0, 0, 0]
for i in range(len(exercise)):
    res[i % 3] += exercise[i]
if res[0] >= res[1] and res[0] >= res[2]:
    print("chest")
elif res[1] >= res[0] and res[1] >= res[2]:
    print("biceps")
else:
    print("back")
