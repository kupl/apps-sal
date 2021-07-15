S = input()

former = int(S[:2])
latter = int(S[2:])

if((former >= 13 or former == 0) and 1 <= latter <= 12):
    print("YYMM")
if((latter >= 13 or latter == 0) and 1 <= former <= 12):
    print("MMYY")
if(1 <= former <= 12 and 1 <= latter <= 12):
    print("AMBIGUOUS")
if((former >= 13 or former == 0) and (latter >= 13 or latter == 0)):
    print("NA")
