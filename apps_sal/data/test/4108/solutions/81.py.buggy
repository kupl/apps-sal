import sys

input = sys.stdin.readline

S = input()
S = S.replace('\n', '')
s_list = list(S)

T = input()
T = T.replace('\n', '')
t_list = list(T)

alpha_dict = {}
t_diff_count = [0 for i in range(27)]
s_diff_count = [0 for i in range(27)]

for i, c in enumerate(range(ord('a'), ord('z') + 1)):
    alpha_dict[chr(c)] = i

for i, s in enumerate(s_list):
    # if not s == t_list[i]:
    number = alpha_dict[s_list[i]]
    s_diff_count[number] += 1
    number = alpha_dict[t_list[i]]
    t_diff_count[number] += 1

for i, s in enumerate(s_list):
    number = alpha_dict[s_list[i]]
    s_count = s_diff_count[number]
    number = alpha_dict[t_list[i]]
    t_count = t_diff_count[number]
    if not s_count == t_count:
        if t_count >= 2:
            print("No")
            return
        if s_count >= 2:
            print("No")
            return
print("Yes")
