S = str(input())
text = [S + 'es' if x == 's' else S + 's' for x in S[-1]]
print(text[0])
