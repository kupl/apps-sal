import sys
input = sys.stdin.readline


def KMP(sentence, word):
    ret = []

    def make_table(word):
        n = len(word)
        table = [0] * (n + 1)
        table[0] = -1
        j = -1
        for i in range(n):
            while j >= 0 and word[i] != word[j]:
                j = table[j]
            j += 1
            table[i + 1] = j
        return table

    table = make_table(word)
    sentence_size = len(sentence)
    word_size = len(word)
    m = 0
    i = 0
    while m + i < sentence_size:
        if word[i] == sentence[m + i]:
            i += 1
            if i == word_size:
                ret.append(m)
                m = m + i - table[i]
                i = table[i]
        else:
            m = m + i - table[i]
            if i > 0:
                i = table[i]
    return ret


n = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
a = []
b = []
for i in range(n):
    a.append(arr1[i] ^ arr1[(i + 1) % n])
    b.append(arr2[i] ^ arr2[(i + 1) % n])
a = (a + a)[:-1]
ks = KMP(a, b)
if len(ks) == 0:
    return
ans = []
for k in ks:
    ans.append((k, arr2[0] ^ arr1[k % n]))
ans = sorted(ans, key=lambda x: x[1])
ans = sorted(ans, key=lambda x: x[0])
for k, x in ans:
    print(k, x)
