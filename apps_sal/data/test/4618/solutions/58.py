s = str(input())
K = int(input())
# sがabcac の場合、a,bca,ac などは部分列(substring
# abc とabの場合、abの方が辞書順で小さいと判断する。
# abc とabaの場合、abaの方が小さい

substrings = set([])
for i in range(5):
    for j in range(len(s) - i):
        # print(i, j)
        substrings.add(s[j:j + i + 1])
# print(substrings)
print((sorted(substrings)[K - 1]))
