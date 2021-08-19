import string
all_string = set(string.ascii_lowercase)
S = set(input())
ans = sorted(list(all_string - S))
print(ans[0]) if ans != [] else print('None')
