def get_score(s, n):
    freq = [0 for i in range(100)]
    for i in range(len(s)):
        freq[ord(s[i]) - 50] += 1
    if n == 0:
        return max(freq)
    elif n == 1:
        if max(freq) == len(s):
            return len(s) - 1
        else:
            return max(freq) + 1
    else:
        return min(len(s), max(freq) + n)


n = int(input())
s1 = input()
s2 = input()
s3 = input()
sc1 = get_score(s1, n)
sc2 = get_score(s2, n)
sc3 = get_score(s3, n)
if sc1 > sc2 and sc1 > sc3:
    print('Kuro')
elif sc2 > sc1 and sc2 > sc3:
    print('Shiro')
elif sc3 > sc1 and sc3 > sc2:
    print('Katie')
else:
    print('Draw')
