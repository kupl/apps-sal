s = input()
print("Good" if all(s[i-1] != s[i] for i in range(1, len(s))) else "Bad")
