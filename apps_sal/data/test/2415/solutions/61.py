elements = [
	'AC','AG','AL','AM','AR','AS','AT','AU','B','BA','BE','BH','BI',
	'BK','BR','C','CA','CD','CE','CF','CL','CM','CN','CO','CR','CS',
	'CU','DB','DS','DY','ER','ES','EU','F','FE','FL','FM','FR','GA',
	'GD','GE','H','HE','HF','HG','HO','HS','I','IN','IR','K','KR',
	'LA','LI','LR','LU','LV','MC','MD','MG','MN','MO','MT','N','NA',
	'NB','ND','NE','NH','NI','NO','NP','O','OG','OS','P','PA','PB','PD',
	'PM','PO','PR','PT','PU','RA','RB','RE','RF','RG','RH','RN','RU','S',
	'SB','SC','SE','SG','SI','SM','SN','SR','TA','TB','TC','TE','TH','TI',
	'TL','TM','TS','U','V','W','XE','Y','YB','ZN','ZR']
 
def in_table(word):
	result = False
	for element in elements:
		if element == word:
			return True
		else:
			if len(word) > len(element) and word[:len(element)] == element:
				result = result or in_table(word[len(element):])
 
	return result
 
def main():
	word = input()
	if in_table(word):
		print('YES')
	else:
		print('NO')
 
def __starting_point():
	main()

__starting_point()
