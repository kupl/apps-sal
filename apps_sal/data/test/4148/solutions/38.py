def rot_n(s, n):
    answer = ''
    for letter in s:
        answer += chr(ord('A') + (ord(letter) - ord('A') + n) % 26)

    return answer

# https://qiita.com/TodayInsane/items/94f495db5ba143a8d3e0


N = int(input())
S = str(input())

print(rot_n(S, N))
