# in the name of god
# Mr_Rubik
# http://codeforces.com/problemset/problem/290/C
foo = baz = 0; quz = 1
for bar in range(1, int(input()) + 1):
    foo += int(input())
    if foo * quz < baz * bar:
        break
    baz, quz = foo, bar
print(baz / quz)
