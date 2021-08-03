S = input()
S = S.replace("/", "")
int_S = int(S)
print("Heisei" if int_S <= 20190430 else "TBD")
