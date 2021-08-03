N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]
a_list = list(set(s))
test_count = 0
for i in range(len(a_list)):
    x = a_list[i]
    if test_count <= s.count(x) - t.count(x):
        test_count = s.count(x) - t.count(x)
print(test_count)
