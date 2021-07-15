elements = set([
	'Ac','Ag','Al','Am','Ar','As','At','Au','B','Ba','Be','Bh','Bi','Bk','Br','C',
	'Ca','Cd','Ce','Cf','Cl','Cm','Cn','Co','Cr','Cs','Cu','Db','Ds','Dy','Er',
	'Es','Eu','F','Fe','Fl','Fm','Fr','Ga','Gd','Ge','H','He','Hf','Hg','Ho','Hs',
	'I','In','Ir','K','Kr','La','Li','Lr','Lu','Lv','Mc','Md','Mg','Mn','Mo','Mt',
	'N','Na','Nb','Nd','Ne','Nh','Ni','No','Np','O','Og','Os','P','Pa','Pb','Pd',
	'Pm','Po','Pr','Pt','Pu','Ra','Rb','Re','Rf','Rg','Rh','Rn','Ru','S','Sb',
	'Sc','Se','Sg','Si','Sm','Sn','Sr','Ta','Tb','Tc','Te','Th','Ti','Tl','Tm',
	'Ts','U','V','W','Xe','Y','Yb','Zn','Zr'
])
 
elem = list(map(lambda x: x.upper(), elements))
 
def find(s):
	if s == "": 
		return True
 
	if s[0] in elem:
		if find(s[1:]):
			return True
 
	if s[0:2] in elem:
		if find(s[2:]):
			return True
	return False

if find(input()):
	print("YES")
else:
	print("NO")
