// Premature optimization is the root of all evil in programming - Knuth.

#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;

#define mod (int) (1e9+7)


ll cubeSum(ll x){
	
	ll sum=0;
	
	while(x){
		ll d=x%10;
		sum+=d;
		x=x/10;
	}
	
	return sum*sum*sum;
	
}


ll dp[5005][5005];


ll recur(vector<ll> &power,ll n,ll r,ll &curr,vector<ll> &vec){
	
	if(r>n){
		return INT_MIN;
	}
	
	if(n==power.size()-1){
		return 0;
	}
	
	ll val=0;
	
	val=max(val,recur(power,n+1,r+1,curr,vec));
	
	val=max(val,power[r]*vec[n]+recur(power,n+1,r,curr,vec));
	
	return val;
	
}



void solve(){
	
	ll n,s; cin>>n>>s;
	
	vector<ll> power(n+1); power[0]=s;
	
	vector<ll> vec(n);
	
	for(int i=0; i<n; i++){
		cin>>vec[i];
	}
	
	for(int i=1; i<=n; i++){
		power[i]=power[i-1]+cubeSum(power[i-1]);
		// cout<<power[i]<<" ";
	}//cout<<endl;
	
	memset(dp,-1,sizeof(dp));
	
	cout<<recur(power,0,0,s,vec)<<"\n";
	
	
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


