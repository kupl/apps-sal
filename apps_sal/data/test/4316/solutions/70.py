from _collections import defaultdict
S = input()

cnt = defaultdict(int)
for i in range(len(S)):
    cnt[S[i]] += 1
    if cnt[S[i]] > 2 or len(cnt) > 2:
        print("No")
        return

print("Yes")

