n = int(input())
s = input()

result = ""

# Aの文字コードに、各文字の文字コードをAの文字コ2ードで企画化？した文字コードにnを足して26で割った余りを足して、文字に戻す
for c in s:
    result += chr(ord("A") + (ord(c) - ord("A") + n) % 26)

print(result)
