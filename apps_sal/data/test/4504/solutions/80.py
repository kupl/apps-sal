S: str = input()
for i in range(len(S) - 2, 0, -2):
    words: str = S[:i]
    half: int = len(words) // 2
    if words[:half] == words[half:]:
        print(half * 2)
        break
