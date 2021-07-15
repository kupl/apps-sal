s = ["AC", "AG", "AL", "AM", "AR", "AS", "AT", "AU", "BA", "BE", "BH", "BI",
     "BK", "BR", "B", "CA", "CD", "CE", "CF", "CL", "CM", "CN", "CO", "CR",
	 "CS", "CU", "C", "DB", "DS", "DY", "ER", "ES", "EU", "FE", "FL", "FM",
	 "FR", "F",  "GA", "GD", "GE", "HE", "HF", "HG", "HO", "HS", "H", "IN",
	 "IR", "I",  "KR", "K",  "LA", "LI", "LR", "LU", "LV", "MC", "MD", "MG",
	 "MN", "MO", "MT", "NA", "NB", "ND", "NE", "NH", "NI", "NO", "NP", "N",
	 "OG", "OS", "O", "PA", "PB", "PD", "PM", "PO", "PR", "PT", "PU", "P",
	 "RA", "RB", "RE", "RF", "RG", "RH", "RN", "RU", "SB", "SC", "SE", "SG",
	 "SI", "SM", "SN", "SR", "S", "TA", "TB", "TC", "TE", "TH", "TI", "TL",
	 "TM", "TS", "U", "V",  "W", "XE", "YB", "Y",  "ZN", "ZR"]
def DFS(a):
    if a is "":
        return "YES"
    for j in s:
        if (len(j)==1 and a[0]==j[0] and DFS(a[1:])=="YES") or (len(a)>=2 and len(j)==2 and a[0]==j[0] and a[1]==j[1] and DFS(a[2:])=="YES"):
            return "YES"
    return "NO"
 
ss = input()
print(DFS(ss))

