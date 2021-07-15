// Premature optimization is the root of all evil in programming - Knuth.

#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

#define mod (int) (1e9+7)


ll digitsSumCube(ll x){
	
	ll sum=0;
	
	while(x){
		sum+=x%10;
		x=x/10;
	}
	
	sum=sum*sum*sum;
	
	return sum;
	
}


ll recur(vector<ll> &energy,ll ind,ll s,ll e){
	
	if(ind>=energy.size()){
		return e;
	}
	
	ll add=digitsSumCube(s);
	
	return max(recur(energy,ind+1,s+add,e),recur(energy,ind+1,s,e+s*energy[ind]));
	
}


void solve(){
	
	ll n,s; cin>>n>>s;
	
	vector<ll> energy(n);
	
	for(int i=0; i<n; i++){
		cin>>energy[i];
	}
	
	cout<<recur(energy,0,s,0)<<"\n";
	
	return ;
	
}




int main(){
    ios_base::sync_with_stdio(0);
    
    cin.tie(0);
    
    int t=1;//cin>>t;
    
    // clock_t begin, end;
    
    // double time_spent;
    
    // begin = clock(); // Time taken till now.
    
    while(t--){
    
	  solve();
        
    }
   
   //end= clock(); // Total  Time taken till now.
   
   //time_spent= (end- begin) / CLOCKS_PER_SEC; 
   
   //cout<<time_spent<<"\n";
   
   
   
	
	return 0;
}


