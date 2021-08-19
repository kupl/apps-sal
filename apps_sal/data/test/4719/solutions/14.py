N = int(input())
let = [0] * 26
S = input()
for a in range(len(S)):
    let[ord(S[a]) - ord('a')] += 1
for i in range(N - 1):
    S = input()
    let_S = [0] * 26
    for j in range(len(S)):
        let_S[ord(S[j]) - ord('a')] += 1
    for k in range(26):
        if let[k] > let_S[k]:
            let[k] = let_S[k]
ans = ''
for l in range(26):
    ans += chr(ord('a') + l) * let[l]
print(ans)
