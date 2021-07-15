texts = list(map(str, input().split()))

result = ""
for text in texts:
    result = result + text[0].upper()
print(result)
