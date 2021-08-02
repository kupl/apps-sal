N = int(input())
S = T = input()

while "()" in S:
    S = S.replace("()", "")

print("(" * S.count(")") + T + S.count("(") * ")")
